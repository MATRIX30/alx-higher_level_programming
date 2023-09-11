#include "lists.h"
#include <stdio.h>
/**
* is_palindrome - this function tells if a linked list is a palindrome or not
* @head: -pointer to the head
* Return: - 1 if palindrome 0 otherwise
*/

int is_palindrome(listint_t **head)
{
	int l[2000];
	int fp = 0, bp = 0, n = 0;
	listint_t *current = *head;

	if (*head == NULL || current->next == NULL)
		return (1);

	while (current != NULL)
	{
		l[n] = current->n;
		current = current->next;
		n += 1;

	}


	bp = n - 1;

	while (fp != bp && fp < n)
	{
		/*printf("%d <==> %d\n",l[fp],l[bp]);*/
		if (l[fp] != l[bp])
		{
			/*printf("%d <==> %d\n",l[fp],l[bp]);*/
			return (0);
		}
		fp = fp + 1;
		bp = bp - 1;
	}
	return (1);
}
