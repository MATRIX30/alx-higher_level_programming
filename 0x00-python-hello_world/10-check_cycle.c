#include "lists.h"
#include <stdio.h>
/**
* check_cycle - this function checks for cycle in single linked list
* @list: the list to be checked
* Return: 0 if there is no cycle and 1 if otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	if (list == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list;
	while (slow->next != NULL)
	{
		if (fast->next->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
