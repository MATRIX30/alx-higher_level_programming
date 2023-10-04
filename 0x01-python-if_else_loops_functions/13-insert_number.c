#include "lists.h"
#include <stdio.h>
/**
 * insert_node - function to insert into a sorted linked list
 * @head: pointer to the head node of list
 * @number: the number to insert to the list
 * Return: pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number);
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *cur, *prev;

	if (*head == NULL)
	{
		return (add_nodeint_end(head, number));
	}
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	cur = *head;
	prev = *head;

	while (cur->next != NULL)
	{

		if (cur->n >= number && cur == *head)
		{
			*head = new_node;
			new_node->next = cur;
			return (new_node);
		}

		cur = cur->next;
		if (cur->n >= number)
		{
			if (cur == *head)
			{
				*head = new_node;
				new_node->next = cur;
				return (new_node);
			}
			prev->next = new_node;
			new_node->next = cur;
			return (new_node);
		}
		if (cur->next != NULL)
		{
			prev = prev->next;
		}
	}

	if (cur->n >= number)
	{
		if (cur == *head)
		{
			*head = new_node;
			new_node->next = cur;
			return (new_node);
		}
		prev->next = new_node;
		new_node->next = cur;
		return (new_node);
	}
	else
	{
		return (add_nodeint_end(head, number));
	}
}
